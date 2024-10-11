import express, { Router } from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import db from './db.js';
import userRouter from './route/userRouter.js';
import itemRouter from './route/itemRouter.js';
import ReportRouter from './route/reportRouter.js';
import rateRouter from './route/rateRoute.js';

const app = express();
const port = 3001;

db.connect();
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.use(cors());

app.use(userRouter);
app.use(itemRouter);
app.use(ReportRouter);
app.use(rateRouter);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
