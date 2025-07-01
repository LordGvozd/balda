import "../styles/components/field_cell.css";

interface FieldCellProps {
	letter: string,
}

const FieldCell = ({ letter }: FieldCellProps) => {
	return(
		<div className="cell">
			{letter}
		</div>
	);
}

export default FieldCell;
