let userId = localStorage.getItem('user_id');
if (!userId) {
  userId = crypto.randomUUID();
  localStorage.setItem('user_id', userId);
}


async function fetchTasks() {
  const res = await fetch('/tasks');
  const tasks = await res.json();

  const list = document.getElementById('taskList');
  list.innerHTML = '';

  tasks.forEach(task => {
    const item = document.createElement('li');
    item.className = task.status ? 'completed' : '';

    item.innerHTML = `
      <div class="task-info">
        <strong>${task.name}</strong> 
        <small>Deadline: ${task.deadline || 'None'}</small>
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

  // Attach event listeners AFTER list is built
  document.querySelectorAll('.complete-btn').forEach(button => {
    button.addEventListener('click', async () => {
      const id = button.getAttribute('data-id');
      await fetch(`/tasks/${id}/toggle`, { method: 'PATCH' });
      fetchTasks();
    });
  });

  document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', async () => {
      const id = button.getAttribute('data-id');
      await fetch(`/tasks/${id}`, { method: 'DELETE' });
      fetchTasks();
    });
  });
}

document.getElementById('taskForm').addEventListener('submit', async e => {
  e.preventDefault();

  const name = document.getElementById('taskName').value;
  const deadline = document.getElementById('deadline').value;

  await fetch('/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, deadline })
  });

  document.getElementById('taskForm').reset();
  fetchTasks();
});

fetchTasks();
