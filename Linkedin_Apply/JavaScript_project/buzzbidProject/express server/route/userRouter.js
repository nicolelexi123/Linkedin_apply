import express from 'express';
import {
  loginUser,
  RegisterUser,
  getPostionByUserName,
} from '../controller/login_register_controller.js';

const userRouter = express.Router();

userRouter.post('/login', loginUser);
userRouter.post('/register', RegisterUser);
userRouter.get('/mainmenu/:username', getPostionByUserName);

export default userRouter;
