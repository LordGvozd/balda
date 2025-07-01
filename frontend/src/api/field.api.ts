import axios from "axios";

import type { IField } from "../types/field.ts";

const API_URL: string = "http://localhost:5000/api";

export const getStartField = async (): Promise<IField> => {
	/*
	 Returns start game field
	 state promise.
	*/
	try {
		const response = await axios.post(`${API_URL}/start-field`);
		return({rows: response.data});
	} catch(error) {
		console.error("An error occured while api request start-field");
		console.error(error);
		throw(error);
	}
}	
