import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';
import Login from './component/LoginAndRegister/Login';
import Register from './component/LoginAndRegister/Register';
import MainMenu from './component/main menu/user/mainMenu';
import ListItem from './component/main menu/user/listItem';
import SearchItem from './component/main menu/user/searchItem';
import SearchResultForm from './component/main menu/user/searchResultForm';
import ItemResult from './component/main menu/user/itemResult';
import ViewRatings from './component/main menu/user/viewRatings';
import AuctionResult from './component/main menu/user/auctionresult';
import ItemDescription from './component/main menu/user/itemDescription';
import AuctionStatistics from './component/main menu/report/AuctionStatistics';
import CancelledAuctionDetails from './component/main menu/report/CancelledAuctionDetails';
import CategoryReport from './component/main menu/report/categoryReport';
import UserReport from './component/main menu/report/userReport';
import TopRatedItems from './component/main menu/report/TopRatedItems';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [position, setPosition] = useState(null);
  useEffect(() => {
    const storedUser = localStorage.getItem('userInfo');

    if (storedUser && storedUser !== 'undefined') {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  useEffect(() => {
    const savedPosition = localStorage.getItem('userPosition');

    if (savedPosition && savedPosition !== 'undefined') {
      setPosition(savedPosition);
    }
  }, []);

  const handleLogout = () => {
    setUser(null);
    setPosition(null);

    localStorage.clear();
  };

  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/mainMenu"
            element={
              <MainMenu
                user={user}
                position={position}
                onLogout={handleLogout}
              />
            }
          />
          <Route path="/list" element={<ListItem user={user} />} />
          <Route path="/search" element={<SearchItem />} />
          <Route path="/searchresult" element={<SearchResultForm />} />
          <Route
            path="/items/:itemId"
            element={<ItemDescription user={user} position={position} />}
          />
          <Route path="/items/itemresult/:itemId" element={<ItemResult />} />
          <Route
            path="/items/:itemId/rate"
            element={<ViewRatings user={user} position={position} />}
          />
          <Route path="/results" element={<AuctionResult />} />
          <Route path="/category" element={<CategoryReport />} />
          <Route path="/user" element={<UserReport />} />
          <Route path="/top-rated" element={<TopRatedItems />} />
          <Route path="/statistics" element={<AuctionStatistics />} />
          <Route path="/cancelled" element={<CancelledAuctionDetails />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
