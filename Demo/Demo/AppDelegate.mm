//
//  AppDelegate.m
//  Demo
//
//  Created by 郝玉鸿 on 2022/9/5.
//

#import "AppDelegate.h"


@interface AppDelegate ()

@end


@implementation AppDelegate

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    @[ @{@"a" : @"a"}, @{@"b" : @"b"} ];
    @{@"a" : @"a", @"b" : @"b"};
    return YES;
    //    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(loginSuccess:) name:NSNotification.UserLoginSuccessNotificationName object:nil];
}

- (void)printA:(void (^)(NSObject *obj1))block obj:(NSObject *)obj2 {
    block([NSObject new]);
}

@end


@interface Test<T> : NSObject

- (void)print;

- (void)print:(void (^)(NSObject *obj1))block;

@end


@interface Test <T>(SomeCategory)

@end
