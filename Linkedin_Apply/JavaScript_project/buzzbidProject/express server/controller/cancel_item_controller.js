import db from '../db.js';

const cancelItem = async (req, res) => {
  const itemID = req.body.itemID;
  const cancel_by = req.body.cancel_by;

  try {
    // 首先检查用户是否是管理员
    const adminCheckQuery = 'SELECT * FROM AdminUser WHERE username = $1';
    const adminCheckResult = await db.query(adminCheckQuery, [cancel_by]);
    if (adminCheckResult.rows.length === 0) {
      // 如果用户不是管理员
      return res
        .status(403)
        .json({ message: 'Only admin users can cancel items.' });
    }

    // 插入取消记录到CancelItem表
    const insertCancelItemQuery = `
            INSERT INTO CancelItem (cancel_by, itemID, reason)
            VALUES ($1, $2, $3)
        `;
    const reason = req.body.reason || 'No reason provided'; // 如果请求中未提供取消原因，使用默认原因
    await db.query(insertCancelItemQuery, [cancel_by, itemID, reason]);

    res.json({ message: 'Item canceled successfully.' });
  } catch (error) {
    console.error('Error canceling item:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
};

export default cancelItem;
