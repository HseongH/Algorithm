const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const loop = input.shift();

function Node(value) {
  this.value = value;
  this.next = null;
}

function Queue() {
  this.front = null;
  this.rear = null;

  this.isEmpty = () => {
    return Number(this.front === null);
  };

  this.enqueue = (value) => {
    if (this.isEmpty()) {
      this.front = new Node(value);
      this.rear = this.front;

      return;
    }

    this.rear.next = new Node(value);
    this.rear = this.rear.next;
  };

  this.dequeue = () => {
    if (this.isEmpty()) return -1;

    const value = this.front.value;
    this.front = this.front.next;

    return value;
  };
}

const queue = new Queue();
const result = [];

for (let i = 0; i < loop; i++) {
  const [command, value] = input[i].split(' ');

  switch (command) {
    case 'pop':
      result.push(queue.dequeue());
      break;

    case 'size':
      result.push(queue.length);
      break;

    case 'empty':
      result.push(queue.isEmpty());
      break;

    case 'front':
      result.push(queue.front ? queue.front.value : -1);
      break;

    case 'back':
      result.push(queue.isEmpty() ? -1 : queue.rear.value);
      break;

    default:
      queue.enqueue(value);
  }
}

console.log(result.join('\n'));
