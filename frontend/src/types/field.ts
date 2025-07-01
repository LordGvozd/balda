export interface IFieldCell {
	owner: "player" | "bot" | "nobody",
	letter: string | null,
}

export interface IField {
	rows: IFieldCell[][],
}
