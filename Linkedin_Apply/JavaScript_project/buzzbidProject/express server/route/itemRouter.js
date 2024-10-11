import express from 'express';
import searchItem from '../controller/search_item_controller.js';
import listItem from '../controller/list_Item_controller.js';
import { getItemByID, getAuctionEndedItemByID } from '../controller/item_controller.js';
import { updateDescriptionByID } from '../controller/item_controller.js';
import { getRatingsByNameForItemId } from '../controller/rate_controller.js';
import { AuctionResult, getWinner } from '../controller/auction_controller.js';
import { getUserByItemID } from '../controller/login_register_controller.js';
import bidOnItem from '../controller/bid_controller.js';
import cancelItem from '../controller/cancel_item_controller.js';

const itemRouter = express.Router();

itemRouter.get('/search', searchItem);
itemRouter.post('/item', listItem);
itemRouter.get('/items/:id', getItemByID);
itemRouter.get('/items/:id/rate', getRatingsByNameForItemId);
itemRouter.put('/items/:id', updateDescriptionByID);
itemRouter.get('/items/itemresult/:id', getAuctionEndedItemByID);
itemRouter.get('/results', AuctionResult);
itemRouter.get('/users/:itemID', getUserByItemID);
itemRouter.post('/items/bid/:itemID', bidOnItem);
itemRouter.post('/cancel', cancelItem);
itemRouter.get('/results/:itemID', getWinner);

export default itemRouter;
