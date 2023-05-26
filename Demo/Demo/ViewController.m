//
//  ViewController.m
//  Demo
//
//  Created by 郝玉鸿 on 2022/9/5.
//

#import "ViewController.h"


@interface ViewController ()

@end


@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSMutableDictionary *dict = [NSMutableDictionary dictionary];
    [dict setValue:@"1234" forKey:@"test"];
    [dict setValue:@"1234" forKey:@"test1"];
    [dict setValue:nil forKey:nil];
    NSLog(@"%@", dict);

    // Do any additional setup after loading the view.
}

- (void)test {
}

@end
