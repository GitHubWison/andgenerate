public class TestAndv2Activity extends FragmentActivity implements ITestAndv2ActivityView{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityTestAndv2Binding binding = DataBindingUtil.setContentView(this,R.layout.activity_test_andv2);
        binding.setViewmodel(new TestAndv2ActivityViewModel(this));
        initFragments();
    }

    private void initFragments() {
        TestAndv2Fragment testAndv2Fragment = TestAndv2Fragment.newInstance();
        testAndv2Fragment.setViewModel(new TestAndv2ViewModel());
        ActivityUtils.addFragmentToActivity(getSupportFragmentManager(),R.id.test_andv2_framelayout,testAndv2Fragment);
    }
}
