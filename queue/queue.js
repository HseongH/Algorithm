function FixedQueue(capacity) {
    this.capacity = capacity,
    this.que = new Array(this.capacity),
    this.no = 0,
    this.front = 0,
    this.rear = 0,

    function Empty() {
        console.error('큐가 비어 있습니다.');
    },

    function Full() {
        console.error('큐가 가득 차 있습니다.');
    },

    function len() {
        return this.no;
    },

    function isEmpty() {
        return this.no <= 0;
    },

    function isFull() {
        return this.no >= this.capacity;
    },

    function enque(value) {
        if (this.isFull()) {
            throw FixedQueue.Full();
        }

        this.que[this.rear] = value;
        this.rear++;
        this.no++;

        if (this.rear === this.capacity) {
            this.rear = 0;
        }
    },

    function deque() {
        if (this.isEmpty()) {
            throw FixedQueue.Empty();
        }

        const value = this.que[this.front];
        this.front++;
        this.no--;

        if (this.front === this.capacity) {
            this.front = 0;
        }

        return value;
    },

    function peek() {
        if (this.isEmpty()) {
            throw FixedQueue.Empty();
        }

        return this.que[this.front];
    },


    function find(value) {
        for (let i = 0; i < this.no; i++) {
            const idx = (i + this.front) % this.capacity;

            if (this.que[idx] === value) {
                return idx;
            }
        }

        return -1;
    },

    function count(value) {
        let count = 0;

        for (let i = 0; i < this.no; i++) {
            const idx = (i + this.front) % this.capacity;

            if (this.que[idx] === value) {
                count++;
            }
        }

        return count;
    },

    function contains(value) {
        return this.count(value);
    },

    function clear() {
        this.no = 0;
        this.front = 0;
        this.rear = 0;
    },

    function dump() {
        if (this.isEmpty()) {
            throw FixedQueue.Empty();
        } else {
            const printStr = '';
            
            for (let i = 0; i < this.no; i++) {
                const idx = (i + this.front) % this.capacity;

                printStr += `${this.que[idx]} `;
            }

            console.log(printStr);
        }
    }
}
