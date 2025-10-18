"""Small utility to standardize categorical columns (city, gender).

This file exposes handle_categorical_data(df) which safely operates on a
DataFrame. Running the script directly will run a tiny demo so the file
no longer raises NameError when executed by itself.
"""
from typing import Any
import pandas as pd


def handle_categorical_data(df: pd.DataFrame) -> pd.DataFrame:
	"""Return a cleaned copy of `df` with standardized `city` and `gender`.

	- city: strip whitespace and lowercase; empty-like values -> <NA>
	- gender: normalize common variants to 'Male' / 'Female'; keep other values

	Raises TypeError if `df` is not a DataFrame.
	"""
	if not isinstance(df, pd.DataFrame):
		raise TypeError("df must be a pandas DataFrame")

	out = df.copy()

	# Clean `city` when present
	if 'city' in out.columns:
		s = out['city'].astype(str).str.strip()
		# Normalize common empty placeholders to <NA>
		s = s.replace({'': pd.NA, 'nan': pd.NA, 'none': pd.NA, 'NaN': pd.NA})
		# Lowercase when not NA
		out['city'] = s.where(s.isna(), s.str.lower())

	# Clean `gender` when present
	if 'gender' in out.columns:
		s = out['gender'].astype(str).str.strip().str.lower()
		# Map common variants to canonical forms
		mapping = {
			'm': 'Male', 'male': 'Male',
			'f': 'Female', 'female': 'Female'
		}
		s = s.replace({'': pd.NA, 'nan': pd.NA, 'none': pd.NA}).replace(mapping)
		# Ensure others are capitalized (e.g., 'other' -> 'Other')
		out['gender'] = s.where(s.isna(), s.str.capitalize())

	return out


if __name__ == '__main__':
	# Demo so the file can be run standalone without a NameError
	demo = pd.DataFrame({
		'city': [' New York ', 'los angeles', None, 'NaN', 'LONDON'],
		'gender': ['M', 'f', 'male', 'Female', None],
		'age': [34, 28, 45, 23, 37]
	})

	print('Original DataFrame:')
	print(demo)
	cleaned = handle_categorical_data(demo)
	print('\nCleaned DataFrame:')
	print(cleaned)
