def test_open_flow_tab(instance, codex_assert, times):
    res = instance.sfe.open_flow_tab()
    assert codex_assert(res, times.pre_period)
