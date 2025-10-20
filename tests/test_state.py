from fsm.symbol import StateMachineFactory


def test_state():
    # create objects
    factory = StateMachineFactory()
    machine = factory.create_state_machine()
    state1 = factory.create_state()
    state2 = factory.create_state()

    # insert states
    machine.insert_state(state1)
    machine.insert_state(state2)

    # create transition from state1 to state2 on "a"
    transA = factory.create_transition_activator("a")
    state1.add_transition(transA, state2)

    # create transition from
    transTestA = factory.create_transition_activator("a")
    transTestB = factory.create_transition_activator("b")

    # validate only state1 -> state2 has transition
    assert state1.get_next_state(transTestA) == state2
    assert state1.get_next_state(transTestB) == None
    assert state2.get_next_state(transTestA) == None
    assert state2.get_next_state(transTestB) == None
