using Microsoft.VisualStudio.TestTools.UnitTesting;

// TODO Problem 2 - Write and run test cases and fix the code to match requirements.

[TestClass]
public class PriorityQueueTests
{
    [TestMethod]
    // Scenario: Add three items with different priorities and remove one.
    // Expected Result: The highest-priority item is returned.
    // Defect(s) Found: Original Dequeue() skipped last item and did not remove it.
    public void TestPriorityQueue_HighestPriorityRemoved()
    {
        var priorityQueue = new PriorityQueue();
        priorityQueue.Enqueue("Low", 1);
        priorityQueue.Enqueue("Medium", 5);
        priorityQueue.Enqueue("High", 10);
        var result = priorityQueue.Dequeue();
        Assert.AreEqual("High", result);
    }

    [TestMethod]
    // Scenario: Add multiple items with the same high priority.
    // Expected Result: The one that was enqueued first should be removed.
    // Defect(s) Found: Original implementation prioritized later items due to >= check.
    public void TestPriorityQueue_TieBreakerFIFO()
    {
        var priorityQueue = new PriorityQueue();
        priorityQueue.Enqueue("First", 10);
        priorityQueue.Enqueue("Second", 10);
        priorityQueue.Enqueue("Third", 5);
        var result = priorityQueue.Dequeue();
        Assert.AreEqual("First", result);
    }

    // Add more test cases as needed below.
    [TestMethod]
    // Scenario: Dequeue from an empty queue.
    // Expected Result: InvalidOperationException is thrown.
    // Defect(s) Found: None (exception is handled correctly)
    public void TestPriorityQueue_EmptyThrows()
    {
        var priorityQueue = new PriorityQueue();
        Assert.ThrowsException<InvalidOperationException>(() => priorityQueue.Dequeue());
    }
}