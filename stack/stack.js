function FixedStack(capacity = 256) {
    this.capacity = capacity,
    this.stk = new Array(this.capacity),
    this.ptr = 0,

    function Empty() {

    },

    function Full() {

    },

    function isEmpty() {
        return this.ptr <= 0;
    },

    function isFull() {
        return this.ptr >= this.capacity;
    },
    
    function len() {
        return this.ptr;
    },

    function push(value) {
        if (this.isFull()) {
            throw FixedStack.FUll();
        }

        this.stk[this.ptr] = value;
        this.ptr += 1;
    },

    function pop() {
        if (this.isEmpty()) {
            throw FixedStack.Empty();
        }

        this.ptr -= 1;
        return this.stk[this.ptr];
    },

    function peek() {
        if (this.isEmpty()) {
            throw FixedStack.Empty();
        }
        
        return this.stk[this.ptr - 1];
    },

    function find(value) {
        for (let i = this.ptr - 1; i >= 0; i--) {
            if (this.stk[i] === value) {
                return i;
            }
        }

        return -1;
    },

    function count(value) {
        let count = 0;

        for (let i = 0; i < this.ptr; i++) {
            if (this.stk[i] === value) {
                count++;
            }
        }

        return count;
    },

    function contains(value) {
        return this.count(value);
    },

    function clear() {
        this.ptr = 0;
    },

    function dump() {
        if (this.isEmpty) {
            console.log('스택이 비어 있습니다.');
        } else {
            const printArr = [];

            for (let i = 0; i < this.ptr; i++) {
                printArr.push(this.stk[i]);
            }

            console.log(printArr);
        }
    }
}
