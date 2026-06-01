window.addEventListener('DOMContentLoaded', () => {
  const myList = document.querySelector('.my_list');
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');

  addItem.addEventListener('click', () => {
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    myList.appendChild(newLi);
  });

  removeItem.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearList.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});
