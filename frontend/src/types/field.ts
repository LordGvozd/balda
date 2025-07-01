export interface IFieldCell {
	owner: string,
	letter: string | null,
}

export interface IField {
	rows: IFieldCell[][],
}
