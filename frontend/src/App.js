import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [questions, setQuestions] = useState([]);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [feedback, setFeedback] = useState({}); // questionId => feedback

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/quiz')
      .then(res => setQuestions(res.data))
      .catch(err => console.error(err));
  }, []);

  const handleOptionClick = (questionId, selectedOption, correctAnswer) => {
    setSelectedAnswers(prev => ({
      ...prev,
      [questionId]: selectedOption
    }));

    setFeedback(prev => ({
      ...prev,
      [questionId]: selectedOption === correctAnswer ? '✅ Correct!' : '❌ Wrong!'
    }));

    // Auto-clear feedback for this question after 2s
    setTimeout(() => {
      setFeedback(prev => {
        const newFeedback = { ...prev };
        delete newFeedback[questionId];
        return newFeedback;
      });
    }, 2000);
  };

  return (
    <div className="App">
      <h1>Quiz App</h1>
      {questions.map(q => (
        <div key={q.id} className="question-box">
          <h3>{q.question}</h3>
          {q.options.map((opt, i) => (
            <button
              key={i}
              onClick={() => handleOptionClick(q.id, opt, q.answer)}
              disabled={selectedAnswers[q.id] !== undefined} // Disable after answering
              style={{
                backgroundColor: selectedAnswers[q.id] === opt
                  ? (opt === q.answer ? 'lightgreen' : 'salmon')
                  : 'white'
              }}
            >
              {opt}
            </button>
          ))}
          {feedback[q.id] && <p className="feedback">{feedback[q.id]}</p>}
        </div>
      ))}
    </div>
  );
}

export default App;
