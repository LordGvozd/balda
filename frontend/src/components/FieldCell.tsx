import { useState } from "react";
import "../styles/components/field_cell.css";

interface FieldCellProps {
	callback: Function 
	startLetter: string | null,
}

const FieldCell = ({ callback, startLetter }: FieldCellProps) => {
	const [letter, setLetter] = useState<string | null>(startLetter);

	const addLetter = () => {
		/*
		 Changes cell letter
		 if cell is empty and provided
		 letter is correct.
		 Updates game field by calling a callback
		 function.
		 */
		if (letter) {
			alert("Выберите пустую клетку");
			return;
		}
		const userLetter = prompt("Введите букву: ");
		if (userLetter && userLetter.length === 1 && isNaN((Number(userLetter)))) {
			setLetter(userLetter.toUpperCase());
			// Updating game field.
			callback(userLetter);
		} else {
			alert("Некорректная буква");
		}
	}

	return(
		<div className="cell" onClick={addLetter}>
			{
				letter
				?
				letter
				:
				""
			}
		</div>
	);
}

export default FieldCell;
