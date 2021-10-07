'''Subclasses of torch.nn.Module, that are reversible and can be used in the
nodes of the GraphINN class. The only additional things that are
needed compared to the base class is an @staticmethod otuput_dims, and the
'rev'-argument of the forward-method.

Abstract template:

* InvertibleModule

Coupling blocks:

* InvertibleModule
* AllInOneBlock
* NICECouplingBlock
* RNVPCouplingBlock
* GLOWCouplingBlock
* GINCouplingBlock
* AffineCouplingOneSided
* ConditionalAffineTransform

Other learned transforms:

* ActNorm
* IResNetLayer
* InvAutoAct
* InvAutoActFixed
* InvAutoActTwoSided
* InvAutoConv2D
* InvAutoFC
* LearnedElementwiseScaling
* OrthogonalTransform
* HouseholderPerm

Fixed (non-learned) transforms:

* PermuteRandom
* FixedLinearTransform
* Fixed1x1Conv

Graph topology:

* SplitChannel
* ConcatChannel
* Split1D
* Concat1d

Reshaping:

* IRevNetDownsampling
* IRevNetUpsampling
* HaarDownsampling
* HaarUpsampling',
* Flatten
* Reshape

'''

# Import the base class first
from .base import *

# Then all inheriting modules
from .all_in_one_block import *
from .fixed_transforms import *
from .reshapes import *
from .coupling_layers import *
from .graph_topology import *
from .orthogonal import *
from .inv_auto_layers import *
from .invertible_resnet import *
from .gaussian_mixture import *
from .spline_blocks import *

__all__ = [
            'InvertibleModule',
            'AllInOneBlock',
            'ActNorm',
            'HouseholderPerm',
            'IResNetLayer',
            'InvAutoAct',
            'InvAutoActFixed',
            'InvAutoActTwoSided',
            'InvAutoConv2D',
            'InvAutoFC',
            'InvertibleModule',
            'LearnedElementwiseScaling',
            'NICECouplingBlock',
            'RNVPCouplingBlock',
            'GLOWCouplingBlock',
            'GINCouplingBlock',
            'AffineCouplingOneSided',
            'ConditionalAffineTransform',
            'PermuteRandom',
            'FixedLinearTransform',
            'Fixed1x1Conv',
            'SplitChannel',
            'ConcatChannel',
            'Split',
            'Concat',
            'OrthogonalTransform',
            'HouseholderPerm',
            'IRevNetDownsampling',
            'IRevNetUpsampling',
            'HaarDownsampling',
            'HaarUpsampling',
            'Flatten',
            'Reshape',
            'GaussianMixtureModel',
            'CubicSplineBlock',
            'RationalQuadraticSplineBlock',
            ]
