from obproject import ProjectFlow
from metaflow import step

from mymodule.main import add


class HelloFlow(ProjectFlow):
    """
    A flow where Metaflow prints 'Hi'.

    Run this flow to validate that Metaflow is installed correctly.

    """

    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.

        """
        import mymodule

        print("HelloFlow is starting.")
        self.next(self.hello)

    @step
    def hello(self):
        """
        A step for metaflow to introduce itself.

        """
        print("Metaflow says: Hi!")
        print(add(1, 2))
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.

        """
        print("HelloFlow is all done.")


if __name__ == "__main__":
    HelloFlow()
