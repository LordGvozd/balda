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

	return(
		<div className="field">	
			{
				field && field.rows
				?
				field.rows.map((row: IFieldCell[], rowID: number) => {
					return(<div key={rowID} className="row">
						{
							row.map((cell: IFieldCell, cellID: number) => {
								return(<FieldCell key={cellID} letter={cell.letter} />)
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
