import db from '../db.js';

export const getItemByID = async (req, res) => {
  const { id } = req.params;

  const query = `
    SELECT
    Item.itemID ,
    Item.username AS listed_by,
    Item.name , Item.start_bid, Item.description, Category.category_name, Item.condition , Item.returnable, Item.get_it_now , Bid.amount , Bid.datetime , Bid.username,
    Item.start_datetime + interval '1 day' * Item.auction_length AS auction_end_time
    FROM
    Item
    INNER JOIN Category ON Category.categoryID = Item.categoryID
    LEFT JOIN ( SELECT
    itemID, amount, datetime, username
    FROM
    Bid
    WHERE
    itemID = $1
    ORDER BY datetime DESC
    LIMIT 4 ) AS Bid
    ON Item.itemID = Bid.itemID
    WHERE
    Item.itemID = $1
    `;

  try {
    const result = await db.query(query, [id]);
    if (result.rows.length > 0) {
      res.json({
        firstResult: result.rows[0],
        allResult: result.rows,
      });
    } else {
      res.status(404).json({ message: 'Item not found' });
    }
  } catch (error) {
    console.error(error);
    res
      .status(500)
      .json({ message: 'An error occurred while fetching the item.' });
  }
};

export const updateDescriptionByID = async (req, res) => {
  const { id } = req.params;
  const { description } = req.body;
  const updateQuery = 'UPDATE Item SET description = $1 WHERE itemID = $2;';
  const selectQuery = 'SELECT description FROM Item WHERE itemID = $1;';

  try {
    const updateResult = await db.query(updateQuery, [description, id]);

    if (updateResult.rowCount > 0) {
      const selectResult = await db.query(selectQuery, [id]);
      if (selectResult.rows.length > 0) {
        res.json({
          success: true,
          message: 'Description updated successfully.',
          description: selectResult.rows[0].description,
        });
      } else {
        res
          .status(404)
          .json({ success: false, message: 'Item not found after update.' });
      }
    } else {
      res.status(404).json({ success: false, message: 'Item not found.' });
    }
  } catch (error) {
    console.error('Error updating item description:', error);
    res.status(500).json({ success: false, message: 'Internal server error.' });
  }
};

export const getAuctionEndedItemByID = async (req,res) =>{
  const { id } = req.params;

  const query = `
    SELECT
      i.itemID,
      i.name,
      i.description,
      i.min_sale,
      i.start_datetime + interval '1 day' * i.auction_length AS auction_end_time,
      c.category_name,
      i.condition,
      i.returnable,
      i.get_it_now,
      b.amount,
      b.datetime,
      b.bidder
    FROM
      Item i
    INNER JOIN Category c ON i.categoryID = c.categoryID
    LEFT JOIN 
    (
      SELECT * FROM
        (
          SELECT ii.itemID,
            CASE 
              WHEN ci.itemID IS NOT NULL THEN 'CANCELED'
              ELSE CONCAT('$', CAST(ROUND(amount,2) AS VARCHAR))       
            END AS amount,
            CASE 
              WHEN ci.itemID IS NOT NULL THEN ci.datetime
              ELSE b.datetime
            END AS datetime,
            CASE 
              WHEN ci.itemID IS NOT NULL THEN 'Administrator'
              ELSE b.username
            END AS bidder
          FROM
            Item ii
          LEFT JOIN CancelItem ci USING (itemID)
          LEFT JOIN Bid b USING (itemID)
          WHERE
            itemID = $1
      ) AS bid_info
    UNION 
    (
      SELECT itemID, CONCAT('$', CAST(ROUND(amount,2) AS VARCHAR)) amount, datetime, username bidder
      FROM Bid WHERE itemID = $1
    ) 
    )AS b USING (itemID)
    WHERE  i.itemID = $1 
    ORDER BY 
    b.datetime DESC
    LIMIT 4;
  `;

  try {
    const result = await db.query(query, [id]);
    if (result.rows.length > 0) {
      res.json({
        firstResult: result.rows[0],
        allResult: result.rows,
      });
    } else {
      res.status(404).json({ message: 'Item not found' });
    }
  } catch (error) {
    console.error(error);
    res
      .status(500)
      .json({ message: 'An error occurred while fetching the item.' });
  }

};