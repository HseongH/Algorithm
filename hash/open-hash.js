const Status = {
    OCCUPIED: 0,
    EMPTY: 1,
    DELETED: 2
}

function Bucket(key = undefined, value = undefined, stat = Status.EMPTY) {
    this.key = key,
    this.value = value,
    this.stat = stat,

    function set_status(stat) {
        this.stat = stat
    }
}

function OpenHash(capacity) {
    this.capacity = capacity,
    this.table = Array.from({length: this.capacity}, () => new Bucket),

    function hash_value(key) {
        if (key === parseInt(key)) {
            return key % this.capacity;
        }

        return parseInt(CryptoJS.MD5(key), 16) % this.capacity;
    },

    function rehash_value(key) {
        return (this.hash_value(key) + 1) % this.capacity;
    },

    function search_node(key) {
        let hash = this.hash_value(key);
        let p = this.table[hash];

        for (let i = 0; i < self.capacity; i++) {
            if (p.stat === Status.EMPTY) {
                break;
            }

            if (p.stat === Status.OCCUPIED && p.key === key) {
                return p;
            }

            hash = this.rehash_value(hash);
            p = this.table[hash];
        }

        return undefined;
    },

    function search(key) {
        const p = this.search_node(key);

        if (p) {
            return p.value;
        }

        return undefined;
    },

    function add(key, value) {
        if (this.search(key)) {
            return false;
        }

        let hash = this.hash_value(key);
        let p = this.table[hash];

        for (let i = 0; i < this.capacity; i++) {
            const condition = [
                p.stat === Status.EMPTY,
                p.stat === Status.DELETED
            ];

            if (condition.includes(true)) {
                this.table[hash] = new Bucket(key, value, Status.OCCUPIED);
                return true;
            }

            hash = this.rehash_value(hash);
            p = self.table[hash];
        }

        return false;
    },

    function remove(key) {
        const p = this.search_node(key);

        if (p) {
            p.set_status(Status.DELETED);
            return true;
        }

        return false;
    },

    function dump() {
        for (let i = 0; i < this.capacity; i++) {
            const p = this.table[i];
            let str = '';

            str += `${i} `;

            if (p.stat === Status.OCCUPIED) {
                str += `${p.key} (${p.value})`;
            } else if (p.stat === Status.EMPTY) {
                str += '---미등록---';
            } else if (p.stat === Status.DELETED) {
                str += '---삭제 완료---';
            }

            console.log(str);
        }
    }
}
