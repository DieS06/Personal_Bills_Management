import { useSelector } from 'react-redux'
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {

    const [expenses, setExpenses] = useState([]);

    useEffect(() => {
      const fetchExpenses = async () => {
        const response = await axios.get();
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
              {expense.name} - {expense.amount} - {expense.date} - {expense.description}
            </li>
          ))}
        </ul>
      </div>
    );
  };

export default Dashboard