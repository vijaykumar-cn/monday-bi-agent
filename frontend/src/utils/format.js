export function formatCurrency(value) {
  if (value === null || value === undefined) return "₹0";

  const number = Number(value);

  if (number >= 1_000_000_000) {
    return `₹${(number / 1_000_000_000).toFixed(2)}B`;
  }

  if (number >= 1_000_000) {
    return `₹${(number / 1_000_000).toFixed(2)}M`;
  }

  if (number >= 1_000) {
    return `₹${(number / 1_000).toFixed(2)}K`;
  }

  return `₹${number.toFixed(2)}`;
}