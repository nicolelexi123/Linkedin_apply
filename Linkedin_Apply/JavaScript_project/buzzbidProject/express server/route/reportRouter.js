import { TopReport } from '../controller/report_controller.js';
import { CategoryReport } from '../controller/report_controller.js';
import { UserReport } from '../controller/report_controller.js';
import { CancelReport } from '../controller/report_controller.js';
import { AuctionStat } from '../controller/report_controller.js';
import express from 'express';

const ReportRouter = express.Router();

ReportRouter.get('/topRate', TopReport);
ReportRouter.get('/category', CategoryReport);
ReportRouter.get('/userreport', UserReport);
ReportRouter.get('/cancelReport', CancelReport);
ReportRouter.get('/auctionstat', AuctionStat);

export default ReportRouter;
