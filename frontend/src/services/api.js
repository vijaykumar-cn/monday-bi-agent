import axios from "axios";

const api = axios.create({
  baseURL: "https://monday-bi-agent-h73s.onrender.com",
});

export default api;