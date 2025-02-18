from typing import Dict, List

GALAXY_PLATFORMS: Dict[str, List[str]] = {
    'AIX': ['6.1', '7.1', '7.2'],
    'Alpine': [],
    'Amazon': [
        '2013.03',
        '2013.09',
        '2014.03',
        '2014.09',
        '2015.03',
        '2015.09',
        '2016.03',
        '2016.09',
        '2017.03',
        '2017.09',
        '2017.12',
        '2018.03',
        'Candidate',
    ],
    'Amazon Linux 2': [],
    'aos': [],
    'ArchLinux': [],
    'ClearLinux': [],
    'Cumulus': ['2.5', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5'],
    'Debian': [
        'bookworm',
        'bullseye',
        'buster',
        'etch',
        'jessie',
        'lenny',
        'sid',
        'squeeze',
        'stretch',
        'wheezy',
    ],
    'DellOS': ['10', '6', '9'],
    'Devuan': ['ascii', 'beowulf', 'ceres', 'jessie'],
    'DragonFlyBSD': ['5.2', '5.4'],
    'EL': ['5', '6', '7', '8', '9'],
    'eos': [],
    'Fedora': [
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
        '32',
        '33',
        '34',
        '35',
        '36',
    ],
    'FreeBSD': [
        '10.0',
        '10.1',
        '10.2',
        '10.3',
        '10.4',
        '11.0',
        '11.1',
        '11.2',
        '11.3',
        '11.4',
        '12.0',
        '12.1',
        '12.2',
        '13.0',
        '8.0',
        '8.1',
        '8.2',
        '8.3',
        '8.4',
        '9.0',
        '9.1',
        '9.2',
        '9.3',
    ],
    'GenericBSD': [],
    'GenericLinux': [],
    'GenericUNIX': [],
    'Gentoo': [],
    'HardenedBSD': ['10', '11'],
    'IOS': [],
    'Junos': [],
    'macOS': ['Big-Sur', 'Catalina', 'High-Sierra', 'Mojave', 'Monterey', 'Sierra'],
    'MacOSX': [
        '10.10',
        '10.11',
        '10.12',
        '10.13',
        '10.14',
        '10.15',
        '10.7',
        '10.8',
        '10.9',
    ],
    'NXOS': [],
    'OpenBSD': [
        '5.6',
        '5.7',
        '5.8',
        '5.9',
        '6.0',
        '6.1',
        '6.2',
        '6.3',
        '6.4',
        '6.5',
        '6.6',
        '6.7',
        '6.8',
        '6.9',
        '7.0',
    ],
    'opensuse': [
        '12.1',
        '12.2',
        '12.3',
        '13.1',
        '13.2',
        '15.0',
        '15.1',
        '15.2',
        '15.3',
        '42.1',
        '42.2',
        '42.3',
    ],
    'os10': ['all'],
    'PAN-OS': ['7.1', '8.0', '8.1', '9.0'],
    'SLES': [
        '10SP3',
        '10SP4',
        '11',
        '11SP1',
        '11SP2',
        '11SP3',
        '11SP4',
        '12',
        '12SP1',
        '12SP2',
        '12SP3',
        '12SP4',
        '12SP5',
        '15',
        '15SP1',
        '15SP2',
        '15SP3',
    ],
    'SmartOS': [],
    'Solaris': ['10', '11.0', '11.1', '11.2', '11.3', '11.4'],
    'Synology': ['6.0', '6.1', '6.2', '7.0'],
    'TMOS': ['12.1', '13.0', '13.1', '14.0'],
    'Ubuntu': [
        'artful',
        'bionic',
        'cosmic',
        'cuttlefish',
        'disco',
        'eoan',
        'focal',
        'groovy',
        'hirsute',
        'impish',
        'jammy',
        'lucid',
        'maverick',
        'natty',
        'oneiric',
        'precise',
        'quantal',
        'raring',
        'saucy',
        'trusty',
        'utopic',
        'vivid',
        'wily',
        'xenial',
        'yakkety',
        'zesty',
    ],
    'vCenter': ['5.5', '6.0', '6.5', '6.7', '7.0'],
    'Void Linux': [],
    'vSphere': ['5.5', '6.0', '6.5', '6.7', '7.0'],
    'Windows': [
        '2008R2',
        '2008x64',
        '2008x86',
        '2012',
        '2012R2',
        '2016',
        '2019',
        '2022',
    ],
}
