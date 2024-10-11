import db from '../db.js';

const listItem = async (req, res) => {
  try {
    // Assuming req.body contains all fields except itemID
    let {
      name,
      username,
      description,
      category,
      condition,
      start_bid,
      min_sale,
      auction_length,
      get_it_now,
      returnable,
    } = req.body;
    console.log(req.body);

    if (get_it_now.length==0){
      get_it_now=null;
    }

    // Query to get the categoryID based on category name
    const categoryQuery = `SELECT categoryID FROM Category WHERE category_name = $1;`;
    const categoryResult = await db.query(categoryQuery, [category]);
    console.log('categoryResult', categoryResult);
    const categoryid = categoryResult.rows[0].categoryid;

    console.log('categoryId', categoryid);
    const userQuery = `SELECT * FROM AllUser WHERE username = $1;`;
    const userResult = await db.query(userQuery, [username]);

    if (userResult.rows.length === 0) {
      return res
        .status(400)
        .json({ success: false, message: 'Username does not exist.' });
    }
    console.log('username', userResult);

    const itemIDQuery = `SELECT MAX(itemID) FROM Item;`;
    const itemIDResult = await db.query(itemIDQuery);
    let itemID=1;
    if (itemIDResult.rowCount>0){
      itemID = itemIDResult.rows[0].max + 1;
    }
    
    // Query to insert item data into item table
    const query = `
            INSERT INTO item (
                itemID,
                name, 
                username,
                description, 
                categoryID,  
                condition, 
                start_bid, 
                min_sale, 
                auction_length, 
                get_it_now, 
                returnable
            ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9,$10,$11)
            RETURNING itemID;`;
    //console.log('query', query);

    // Execute the query with the values
    const result = await db.query(query, [
      itemID,
      name,
      username,
      description,
      categoryid,
      condition,
      start_bid,
      min_sale,
      auction_length,
      get_it_now,
      returnable,
    ]);

    // Assuming result.rows contains the rows returned by the query
    // Send back the auto-generated itemID to the client, if needed
    res.json({
      success: true,
      message: 'Item listed successfully.',
      itemID: result.rows[0].itemID,
    });
  } catch (error) {
    console.error('Error listing item:', error);
    res.status(500).json({ success: false, message: 'Error listing item.' });
  }
};
export default listItem;
