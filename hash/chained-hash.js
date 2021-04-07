function Node(key, value, next) {
    this.key = key,
    this.value = value,
    this.next = next
}

function ChainedHash(capacity) {
    this.capacity = capacity,
    this.table = new Array(this.capacity),

    function hash_value(key) {
        if (key === parseInt(key)) {
            return key % this.capacity;
        }
        return parseInt(SHA256(key), 16);
    },

    function search(key) {
        const hash = this.hash_value(key);
        let p = this.table[hash];

        while (p) {
            if (p.key === key) {
                return p.value;
            }
            p = p.next;
        }

        return undefined;
    },

    function add(key, value) {
        const hash = this.hash_value(key);
        let p = this.table[hash];

        while (p) {
            if (p.key == key) {
                return false;
            }
            p = p.next;
        }

        const temp = new Node(key, value, this.table[hash]);
        this.table[hash] = temp;
        return true;
    },

    function remove(key) {
        const hash = this.hash_value(key);
        let p = this.table[hash];
        let pp = undefined;

        while (p) {
            if (p.key == key) {
                if (!pp) {
                    this.table[hash] = p.next;
                } else {
                    pp.next = p.next;
                }
                return true;
            }

            pp = p;
            p = p.next;
        }

        return false;
    },

    function dump() {
        for (let i = 0; i < this.capacity; i++) {
            let p = this.table[i];
            let str = '';

            str += i;

            while (p) {
                str += `   ${p.key} (${p.value})`;
                p = p.next;
            }
            console.log(str);
        }
    }
}
