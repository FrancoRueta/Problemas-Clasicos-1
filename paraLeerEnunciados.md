P1 - Cuantos Locks hay definidos y cuál de ellos asegura exclusión mútua a los escritores?


P2 - Del análisis de los métodos r_acquire() y r_release(), que se transcribe a continuación:

    def r_acquire(self):
        self.num_r_lock.acquire()
        self.num_r += 1
        if self.num_r == 1:
            self.w_lock.acquire()
        self.num_r_lock.release()

    def r_release(self):
        assert self.num_r > 0
        self.num_r_lock.acquire()
        self.num_r -= 1
        if self.num_r == 0:
            self.w_lock.release()
        self.num_r_lock.release()

Que cuenta la variable numerica num_r ?