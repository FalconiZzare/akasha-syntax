import axios from "axios";
import { noAuthHeader } from "@/services/headers";

const BASE_URL = "https://li6dit4n0lz7.share.zrok.io";

export const ask = async (data) => {
  return await axios.post(`${BASE_URL}/ask`, data, {
    headers: noAuthHeader()
  });
};
