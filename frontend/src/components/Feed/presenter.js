import React from "react";
import PropTypes from "prop-types";
import { Route, Switch } from "react-router-dom";
import "./styles.scss";

const Feed = props => "Feed!";

Feed.PropTypes = {
  loading: PropTypes.bool.isRequired
};

export default Feed;
