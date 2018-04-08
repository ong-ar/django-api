import Reactotron from "reactotron-react-js";
import { reactotronRedux } from "reactotron-redux";

Reactotron.configure({ name: "django_api" })
  .use(reactotronRedux())
  .connect();

export default Reactotron;
