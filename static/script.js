let userId = localStorage.getItem('user_id');
if (!userId) {
  userId = crypto.randomUUID();
  localStorage.setItem('user_id', userId);
}

async function fetchTasks() {
  const res = await fetch('/tasks', {
    headers: { 'X-User-ID': userId }
  });
  const tasks = await res.json();

  const list = document.getElementById('taskList');
  list.innerHTML = '';

  const priorityLabels = {
  1: 'Low',
  2: 'Medium',
  3: 'High'
};

tasks.forEach(task => {
  const item = document.createElement('li');
  item.className = task.status ? 'completed' : '';

  item.innerHTML = `
    <div class="task-info">
      <strong>${task.name}</strong> 
      <small>Deadline: ${task.deadline || 'None'}</small>
      <small>Priority: <span class="priority-label priority-${task.priority}">${priorityLabels[task.priority] || 'Medium'}</span></small>
    </div>
    <div>
      <button class="complete-btn" data-id="${task.id}">
        ${task.status ? 'Done' : 'Incomplete'}
      </button>
      <button class="delete-btn" data-id="${task.id}">Delete</button>
    </div>
  `;

  list.appendChild(item);
});


  document.querySelectorAll('.complete-btn').forEach(button => {
    button.addEventListener('click', async () => {
      const id = button.getAttribute('data-id');
      await fetch(`/tasks/${id}/toggle`, { 
        method: 'PATCH',
        headers: { 'X-User-ID': userId }
      });
      fetchTasks();
    });
  });

  document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', async () => {
      const id = button.getAttribute('data-id');
      await fetch(`/tasks/${id}`, { 
        method: 'DELETE',
        headers: { 'X-User-ID': userId }
      });
      fetchTasks();
    });
  });
}

const priorityBoxes = document.querySelectorAll('.priority-box');
let selectedPriority = 2;

priorityBoxes.forEach(box => {
  box.addEventListener('click', () => {
    priorityBoxes.forEach(b => b.classList.remove('selected'));
    box.classList.add('selected');
    selectedPriority = parseInt(box.getAttribute('data-value'), 10);
  });
});

document.getElementById('taskForm').addEventListener('submit', async e => {
  e.preventDefault();

  const name = document.getElementById('taskName').value;
  const deadline = document.getElementById('deadline').value;

  await fetch('/tasks', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'X-User-ID': userId
    },
    body: JSON.stringify({ name, deadline, priority: selectedPriority })
  });

  document.getElementById('taskForm').reset();


  priorityBoxes.forEach(b => b.classList.remove('selected'));
  priorityBoxes[1].classList.add('selected');
  selectedPriority = 2;

  fetchTasks();
});



fetchTasks();
