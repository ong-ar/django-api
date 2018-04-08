import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { routerReducer, routerMiddleware } from "react-router-redux";
import createHistory from "history/createBrowserHistory";
import users from "redux/modules/users";

const env = process.env.NODE_ENV;

const history = createHistory();

const middlewares = [thunk, routerMiddleware(history)];

const reducer = combineReducers({
  users,
  routing: routerReducer
});

if (env === "development") {
  const { logger } = require("redux-logger");
  middlewares.push(logger);
}

let store = initialState =>
  createStore(reducer, applyMiddleware(...middlewares));

export { history };

export default store();
