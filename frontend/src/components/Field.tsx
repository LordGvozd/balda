import { useEffect, useState } from "react";

import FieldCell from "./FieldCell";
import type { IField, IFieldCell } from "../types/field";
import { getStartField } from "../api/field.api";
import "../styles/components/field.css";

const Field = () => {
	const [field, setField] = useState<IField | null>(null);

	useEffect(() => {
		getStartField().then((field: IField) => {
			setField(field);
		});
	}, []);

	const updateFieldCell = (rowID: number, cellID: number, userLetter: string) => {
		/*
		 Updates field state after
		 clicking on cell and providing letter
		 by user.
		 This function is a callback for cell component.
		 */

		if (!field || !field.rows) {
			return;
		}
		
		let newField = field;
		newField.rows[rowID][cellID].owner = "player";
		newField.rows[rowID][cellID].letter = userLetter;
		setField(newField);
	}

	return(
		<div className="field">	
			{
				field && field.rows
				?
				field.rows.map((row: IFieldCell[], rowID: number) => {
					return(<div key={rowID} className="row">
						{
							row.map((cell: IFieldCell, cellID: number) => {
								return(
									<FieldCell 
										key={cellID} callback={(userLetter: string) => updateFieldCell(rowID, cellID, userLetter)}
										startLetter={cell.letter} 
									/>
								)
							})
						}
					</div>)
				})
				:
				<></>
			}
		</div>
	);
}

export default Field;
