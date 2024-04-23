import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ExpenseList = () => {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    const fetchExpenses = async () => {
      const response = await axios.get('http://your-backend-domain/api/expenses');
      setExpenses(response.data);
    };

    fetchExpenses();
  }, []);

  return (
    <div>
      <h2>Expenses</h2>
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            {expense.date} - {expense.amount} - {expense.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ExpenseList;
