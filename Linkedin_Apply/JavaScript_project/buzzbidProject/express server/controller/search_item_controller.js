import db from '../db.js';

const searchItem = async (req, res) => {
  try {
    const { keyword, category, condition } = req.query;
    let { minimumPrice, maximumPrice } = req.query;

    minimumPrice = minimumPrice === '' ? null : Number(minimumPrice);
    maximumPrice = maximumPrice === '' ? null : Number(maximumPrice);

    minimumPrice = isNaN(minimumPrice) ? null : minimumPrice;
    maximumPrice = isNaN(maximumPrice) ? null : maximumPrice;
    let processedKeyword = keyword || null;
    const processedCategory = category || null;
    const processedCondition = condition || null;

    if (!/\S/.test(keyword) ){
      processedKeyword=null;
    }

    let conditionArray = [];
    switch (processedCondition) {
      case 'New':
        conditionArray = ['New'];
        break;
      case 'Good':
        conditionArray = ['Very Good', 'New', 'Good'];
        break;
      case 'Very Good':
        conditionArray = ['Very Good', 'New'];
        break;
      case 'Fair':
        conditionArray = ['Very Good', 'New', 'Good', 'Fair'];
        break;
      default:
        conditionArray = ['New', 'Good', 'Very Good', 'Fair', 'Poor'];
    }

    const queryParams = [
      processedKeyword,
      processedCategory,
      conditionArray,
      minimumPrice,
      maximumPrice,
    ];
    console.log(queryParams);

    const queryText = `
    SELECT
    Item.itemID AS ID,
    Item.name AS item_name,
    (SELECT MAX(amount) FROM Bid b WHERE b.itemID = Item.itemID) AS current_bid,
    (SELECT username FROM Bid WHERE Bid.itemID = Item.itemID ORDER BY amount DESC LIMIT 1) AS high_bidder,
    Item.get_it_now AS get_it_now_price,
    Item.start_datetime + interval '1 day' * Item.auction_length AS auction_end_time
  FROM
    Item
  INNER JOIN Category ON Item.categoryID = Category.categoryID
  WHERE
    ($1::text IS NULL OR Item.name LIKE '%' || $1 || '%' OR Item.description LIKE '%' || $1 || '%')
    AND ($2::text IS NULL OR Category.category_name = $2)
    AND (Item.condition = ANY($3))
    AND (
      $4::numeric IS NULL
      OR (
          SELECT
              CASE
                  WHEN MAX(amount) IS NULL THEN Item.start_bid
                  ELSE COALESCE(MAX(amount), Item.start_bid)
              END
          FROM
              Bid
          WHERE
              Bid.itemID = Item.itemID
      ) >= $4
    )
    AND (
      $5::numeric  IS NULL
      OR (
          SELECT
              CASE
                  WHEN MAX(amount) IS NULL THEN Item.start_bid
                  ELSE COALESCE(MAX(amount), Item.start_bid)
              END
          FROM
              Bid
          WHERE
              Bid.itemID = Item.itemID
      ) <= $5      
    )
    AND NOT EXISTS (
      SELECT 1 FROM CancelItem WHERE CancelItem.itemID = Item.itemID
    )
    AND Item.start_datetime + interval '1 day' * Item.auction_length > CURRENT_TIMESTAMP
    AND (Item.get_it_now is null OR ((SELECT MAX(amount) FROM Bid WHERE Bid.itemID = Item.itemID) < Item.get_it_now) OR (SELECT MAX(amount) FROM Bid WHERE Bid.itemID = Item.itemID) IS NULL)
  ORDER BY
    auction_end_time ASC;
  
`;

    const { rows } = await db.query(queryText, queryParams);

    res.json(rows);
  } catch (error) {
    console.error('Query error', error.message, error.stack);
    res.status(500).send('Internal Server Error');
  }
};
export default searchItem;
