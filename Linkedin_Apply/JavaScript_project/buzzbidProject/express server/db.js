import pg from 'pg';

const db = new pg.Client({
  user: 'postgres',
  host: 'localhost',
  database: 'buzzdemo',
  password: 'newpassword',
  port: 5432,
});

export default db;
