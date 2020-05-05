from pynwb import register_class
from pynwb.file import LabMetaData, DynamicTable
from hdmf.utils import docval, call_docval_func, get_docval


@register_class('EcephysExt', 'ndx-bipolar-scheme')
class EcephysExt(LabMetaData):
    """
    Meta data for bipolar scheme
    """
    __nwbfields__ = ('ecephys_ext',)

    @docval(dict(name='ecephys_ext', type=str, doc='name of this EcephysExt', default='EcephysExt'),  # required
            *get_docval(LabMetaData.__init__))
    def __init__(self, **kwargs):
        call_docval_func(super(EcephysExt, self).__init__, kwargs)


@register_class('BipolarSchemeTable', 'ndx-bipolar-scheme')
class BipolarSchemeTable(DynamicTable):
    """
    Table for storing bipolar scheme data
    """

    __columns__ = (
        {'name': 'anodes', 'description': 'references the electrodes table', 'required': True, 'index': True},
        {'name': 'cathodes', 'description': 'references the electrodes table', 'required': True, 'index': True}
    )

    @docval(dict(name='name', type=str, doc='name of this BipolarSchemeTable',
                 default='BipolarSchemeTable'),  # required
            dict(name='description', type=str, doc='Description of this DynamicTableRegion',
                 default='references the electrodes table'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(BipolarSchemeTable, self).__init__, kwargs)
