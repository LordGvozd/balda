import "../styles/components/field_cell.css";

interface FieldCellProps {
	letter: string | null,
}

const FieldCell = ({ letter }: FieldCellProps) => {
	return(
		<div className="cell">
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
