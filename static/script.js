// Get or create user_id and store in localStorage
let userId = localStorage.getItem('user_id');
if (!userId) {
  userId = crypto.randomUUID();
  localStorage.setItem('user_id', userId);
}

// Elements for confirmation popup
const confirmPopup = document.getElementById('confirm-popup');
const confirmYes = document.getElementById('confirm-yes');
const confirmNo = document.getElementById('confirm-no');
let taskIdToDelete = null;

// Fetch and render tasks
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
}

// Event delegation for complete/delete buttons
document.getElementById('taskList').addEventListener('click', async (e) => {
  if (e.target.classList.contains('complete-btn')) {
    const id = e.target.getAttribute('data-id');
    await fetch(`/tasks/${id}/toggle`, { 
      method: 'PATCH',
      headers: { 'X-User-ID': userId }
    });
    fetchTasks();
  }

  if (e.target.classList.contains('delete-btn')) {
    taskIdToDelete = e.target.getAttribute('data-id');
    confirmPopup.classList.remove('hidden');
  }
});

// Confirmation popup actions
confirmYes.addEventListener('click', async () => {
  if (taskIdToDelete) {
    await fetch(`/tasks/${taskIdToDelete}`, { 
      method: 'DELETE',
      headers: { 'X-User-ID': userId }
    });
    taskIdToDelete = null;
    confirmPopup.classList.add('hidden');
    fetchTasks();
  }
});

confirmNo.addEventListener('click', () => {
  taskIdToDelete = null;
  confirmPopup.classList.add('hidden');
});

// Priority selection
const priorityBoxes = document.querySelectorAll('.priority-box');
let selectedPriority = 2;

// Set initial selected priority
priorityBoxes.forEach(b => b.classList.remove('selected'));
priorityBoxes[1].classList.add('selected');

priorityBoxes.forEach(box => {
  box.addEventListener('click', () => {
    priorityBoxes.forEach(b => b.classList.remove('selected'));
    box.classList.add('selected');
    selectedPriority = parseInt(box.getAttribute('data-value'), 10);
  });
});

// Form submission
document.getElementById('taskForm').addEventListener('submit', async e => {
  e.preventDefault();

  const name = document.getElementById('taskName').value.trim();
  const deadline = document.getElementById('deadline').value;

  if (!name) {
    alert('Please enter a task name.');
    return;
  }

  await fetch('/tasks', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'X-User-ID': userId
    },
    body: JSON.stringify({ name, deadline, priority: selectedPriority })
  });

  document.getElementById('taskForm').reset();

  // Reset priority selection
  priorityBoxes.forEach(b => b.classList.remove('selected'));
  priorityBoxes[1].classList.add('selected');
  selectedPriority = 2;

  fetchTasks();
});

// Initial fetch of tasks when page loads
fetchTasks();
