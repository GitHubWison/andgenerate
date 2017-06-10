public class TestAndv2Fragment extends Fragment implements ITestAndv2FragmentView{
private TestAndv2ViewModel viewModel;
    public TestAndv2Fragment() {
        // Required empty public constructor
    }

    public static Fragment newInstance() {
        
        Bundle args = new Bundle();
        
        TestAndv2Fragment fragment = new TestAndv2Fragment();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        FragmentTestAndv2Binding binding = FragmentTestAndv2Binding.inflate(inflater,container,false);
        binding.setViewmodel(viewModel);
        return binding.getRoot();
    }

    public void setViewModel(TestAndv2ViewModel viewModel) {
        this.viewModel = viewModel;
    }
}
