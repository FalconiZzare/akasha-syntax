import axios from "axios";
import { noAuthHeader } from "@/services/headers";

const BASE_URL = "https://api.akashasolutions.com";

export const ask = async (data) => {
  return await axios.post(`${BASE_URL}/ask`, data, {
    headers: noAuthHeader()
  });
};
