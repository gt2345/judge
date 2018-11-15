from dmoj.result import Result
from dmoj.graders import StandardGrader

class Grader(StandardGrader):
    def grade(self, case):
        print('Interacting for case 18')

        res = Result(case)

        input = 'Hello, World!\n'

        self._current_proc = self.binary.launch(time=self.problem.time_limit, memory=self.problem.memory_limit,
                                            pipe_stderr=True, io_redirects=case.io_redirects(),
                                            wall_time=case.config.wall_time_factor * self.problem.time_limit)

        output, error = self._current_proc.safe_communicate(input + '\n')
        print("input：" + input)
        print("output：" + output)
        print(output == input)
        if output == input:
            res.result_flag = Result.AC
            res.proc_output = 'Correct answer! This will be displayed in the partial output pane.'
        else:
            res.result_flag = Result.WA
            res.proc_output = 'Wrongggggg answer! :('

        return res

