<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Habit Tracker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f6f9;
      margin: 0;
      padding: 20px;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    .habit-form {
      display: flex;
      justify-content: center;
      margin-bottom: 20px;
    }
    .habit-form input {
      padding: 10px;
      width: 60%;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin-right: 10px;
    }
    .habit-form button {
      padding: 10px 15px;
      border: none;
      border-radius: 8px;
      background: #4CAF50;
      color: white;
      cursor: pointer;
    }
    .habit-form button:hover {
      background: #45a049;
    }
    ul {
      list-style: none;
      padding: 0;
      max-width: 600px;
      margin: 0 auto;
    }
    li {
      background: white;
      padding: 15px;
      margin-bottom: 10px;
      border-radius: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }
    li.completed {
      text-decoration: line-through;
      color: gray;
      background: #e0ffe0;
    }
    .complete-btn {
      background: #008CBA;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 8px;
      cursor: pointer;
    }
    .complete-btn:hover {
      background: #007bb5;
    }
  </style>
</head>
<body>
  <h1>Habit Tracker</h1>

  <div class="habit-form">
    <input type="text" id="habitInput" placeholder="Enter a habit...">
    <button onclick="addHabit()">Add Habit</button>
  </div>

  <ul id="habitList"></ul>

  <script>
    function addHabit() {
      const input = document.getElementById("habitInput");
      const habitText = input.value.trim();
      if (habitText === "") return;

      const li = document.createElement("li");
      li.innerHTML = `
        <span>${habitText}</span>
        <button class="complete-btn" onclick="toggleHabit(this)">Done</button>
      `;
      document.getElementById("habitList").appendChild(li);
      input.value = "";
    }

    function toggleHabit(button) {
      const li = button.parentElement;
      li.classList.toggle("completed");
    }
  </script>
</body>
</html>
