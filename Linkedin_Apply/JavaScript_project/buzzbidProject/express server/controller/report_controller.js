import db from '../db.js';

export const TopReport = async (req, res) => {
  try {
    const query = ` SELECT 
        i.name, ROUND(AVG(r.rating),1) avg_rating, count(r.rating) as rating_ct
        FROM Item i
        JOIN Rating r ON i.itemID = r.itemID
        GROUP BY 1
        ORDER BY avg_rating DESC, LOWER(i.name) ASC
        LIMIT 10;
        
        `;
    const { rows } = await db.query(query);

    res.send(rows);
  } catch (error) {
    console.error('Error occurred while generating category report:', error);

    res.status(500).json({ message: 'Internal Server Error' });
  }
};
export const CategoryReport = async (req, res) => {
  try {
    const query = ` SELECT 
      Category.category_name AS Category,
      COUNT(DISTINCT Item.itemID) AS Total_Items,
      MIN(Item.get_it_now) AS Min_Price,
      MAX(Item.get_it_now) AS Max_Price,
      ROUND(AVG(CASE WHEN Item.get_it_now IS NOT NULL THEN Item.get_it_now END), 2) AS Average_Price
      FROM 
      Item
      INNER JOIN 
      Category ON Item.categoryID = Category.categoryID
      LEFT JOIN 
      CancelItem ON Item.itemID =  CancelItem.itemID
      WHERE 
      CancelItem.itemID IS NULL
      GROUP BY 
      Category.category_name
      ORDER BY 
      Category.category_name
      `;

    const { rows, rowCount } = await db.query(query);

    res.send(rows);
  } catch (error) {
    console.error('Error occurred while generating category report:', error);

    res.status(500).json({ message: 'Internal Server Error' });
  }
};
export const UserReport = async (req, res) => {
  try {
    const query = ` with t1 as (
      select itemid, username, amount as max_bid
      from
           (SELECT itemID,username,amount, row_number() over (partition by itemid  order by amount desc) rn
        FROM Bid
         )sub1
      where rn =1),
    t2 as (
    select username,count(distinct i.itemid) as listed
      from item i group by 1
    ),
    t3 as (
    select t1.username,count(distinct i.itemid) as won
    from item i left join t1
    on i.itemid = t1.itemid 
      where 
    ((NOW() > (i.start_datetime+interval '1 day' * i.auction_length)
              AND t1.max_bid >= i.min_sale)
              OR (t1.max_bid  =  i.get_it_now) )
      group by 1
    ),
    t4 as (
    select rated_by, count(distinct itemid) rated from rating group by 1
    ),
    t5 as (
      select username,condition from (
      select *,row_number() over (partition by username order by ct DESC, condition_rank DESC ) rn from (
      select username,condition,condition_rank,count(condition_rank) ct
      from(
    select *,case when condition = 'New' Then 1
      when condition = 'Very Good' Then 2
      when condition = 'Good' Then 3
      when condition = 'Fair' Then 4
      when condition= 'Poor' Then 5
      end as condition_rank
      from item )sub2
      group by 1,2,3
      )sub3 )sub4
      where rn = 1
    ),
    t6 as (
    select i.username,count(distinct i.itemid) as sold
    from item i
    join t1
    on i.itemid = t1.itemid 
      where 
    ((NOW() > (i.start_datetime+interval '1 day' * i.auction_length)
              AND t1.max_bid >= i.min_sale)
              OR (t1.max_bid  =  i.get_it_now) )
      group by 1
    )
    select al.username,
    coalesce(listed,0) as listed,
    coalesce(sold,0) as sold,
    coalesce(won,0) as won,
    coalesce(rated,0) as rated,
    coalesce(condition,'NA') as most_frequent_condition
    from alluser al left join t2
    on al.username = t2.username
    left join t3 on al.username = t3.username
    left join t4 on al.username = t4.rated_by
    left join t5 on al.username = t5.username
    left join t6 on al.username = t6.username
    order by listed DESC
    
          `;
    const { rows, rowCount } = await db.query(query);

    res.send(rows);
  } catch (error) {
    console.error('Error occurred while generating category report:', error);

    res.status(500).json({ message: 'Internal Server Error' });
  }
};
export const AuctionStat = async (req, res) => {
  try {
    const query = ` with t1 as (
          SELECT itemID, max(amount) max_bid
          FROM
          Bid
          GROUP BY 1
          ),
          t2 as(
          SELECT 'Auctions Active' as type, COUNT(*)  ct
          FROM Item i
          LEFT JOIN CancelItem c ON i.itemID = c.itemID
          LEFT JOIN  t1 ON i.itemID = t1.itemID
          Where c.datetime is Null
          AND NOW() < (i.start_datetime+interval '1 day' * i.auction_length)
          AND ((i.get_it_now is Null) or (t1.max_bid is Null) or (t1.max_bid < i.get_it_now)) ),
          t3 as(
          SELECT 'Auctions Won' as type, COUNT(*)  ct
          FROM Item i
          LEFT JOIN CancelItem c ON i.itemID = c.itemID
          JOIN  t1 on i.itemID = t1.itemID
          Where c.datetime is Null
          AND 
          ((NOW() > (i.start_datetime+interval '1 day' * i.auction_length)
          AND t1.max_bid >= i.min_sale)
          OR (t1.max_bid  =  i.get_it_now) )),
          t4 as (
          SELECT 'Auctions Finished' as type, COUNT(*)  ct
          FROM Item i
          LEFT JOIN CancelItem c ON i.itemID = c.itemID
          LEFT JOIN t1 on i.itemID = t1.itemID
          Where c.datetime is Null
          AND ( (NOW() >(i.start_datetime+interval '1 day' * i.auction_length) )
          OR (t1.max_bid  =  i.get_it_now) )
          ),t5 as(
          SELECT
          'Auctions Cancelled' as type, COUNT(*)  ct
          FROM CancelItem
          ),t6 as(
          SELECT
          'Items Rated' as type,COUNT(*)  ct
          FROM Rating),
          t7 as (
          SELECT
          'Items Not Rated' as type, COUNT(*)  ct
          FROM
          Item i
          LEFT JOIN CancelItem c ON i.itemID = c.itemID
          JOIN t1 ON i.itemID = t1.itemID 
          LEFT JOIN Rating r ON r.itemID  = i.itemID
          Where c.datetime is Null
          AND (
            (
            NOW() > (i.start_datetime+interval '1 day' * i.auction_length)
            AND (t1.max_bid >= i.min_sale)
            )
            OR (t1.max_bid  =  i.get_it_now) 
          )
          AND r.rate_datetime is Null
          )
          
          select * from t2 
          UNION ALL 
          select * from t4
          UNION ALL 
          select * from t3
          UNION ALL 
          select * from t5
          UNION ALL 
          select * from t6
          UNION ALL 
          select * from t7
          
      
      `;

    const { rows, rowCount } = await db.query(query);

    res.send(rows);
  } catch (error) {
    console.error('Error occurred while generating category report:', error);

    res.status(500).json({ message: 'Internal Server Error' });
  }
};

export const CancelReport = async (req, res) => {
  try {
    const query = ` SELECT
      i.itemID, i.username, TO_CHAR(c.datetime, 'yyyy-mm-dd hh12:miAM') as date, c.reason FROM
      Item i
      JOIN CancelItem c ON i.itemID = c.itemID
      ORDER BY i.itemID DESC
      `;

    const { rows, rowCount } = await db.query(query);

    res.send(rows);
  } catch (error) {
    console.error('Error occurred while generating category report:', error);

    res.status(500).json({ message: 'Internal Server Error' });
  }
};
