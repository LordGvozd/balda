import { useEffect, useState } from "react";

import FieldCell from "./FieldCell";

import "../styles/components/field.css";

const Field = () => {
	const [fieldMatrix, setFieldMatrix] = useState<string[][]>([]);

	useEffect(() => {
		setFieldMatrix(
			[
				["", "", ""],
				["Л", "О", "Х"],
				["", "", ""],
			]
		);
	}, []);

	return(
		<div className="field">	
			{
				fieldMatrix.map((row: string[], rowID: number) => {
					return(<div key={rowID} className="row">
						{
							row.map((cellLetter: string, cellID: number) => {
								return(<FieldCell key={cellID} letter={cellLetter} />)
							})
						}
					</div>)
				})
			}
		</div>
	);
}

export default Field;
