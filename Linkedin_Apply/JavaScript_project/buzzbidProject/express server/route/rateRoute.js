import express from 'express';

import {
  rateAdd,
  rateDel,
  getRateByItemidanduser,
} from '../controller/rate_controller.js';
const rateRouter = express.Router();

rateRouter.post('/rate', rateAdd);
rateRouter.delete('/rate', rateDel);
rateRouter.get('/rate/:itemid/:rated_by', getRateByItemidanduser);

export default rateRouter;
